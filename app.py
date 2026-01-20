from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from sqlalchemy import extract
import os


app = Flask(__name__)

# --- CONFIGURATION ---
SECRET_KEY = "shift77" 

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "shiftlog.db"))
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class WorkDay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True, nullable=False)
    employer = db.Column(db.String(100))
    start_time = db.Column(db.String(5))
    end_time = db.Column(db.String(5))
    break_minutes = db.Column(db.Integer, default=0)
    total_hours = db.Column(db.Float)

with app.app_context():
    db.create_all()

# Block the main root so people can't stumble upon it
@app.route('/')
def lock_root():
    abort(404)

@app.route(f'/{SECRET_KEY}', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date_str = request.form.get('manual_date')
        entry_date = datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else date.today()
        start, end = request.form.get('start'), request.form.get('end')
        brk, emp = request.form.get('break'), request.form.get('employer')
        fmt = '%H:%M'
        
        try:
            tdelta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            hrs = round((tdelta.total_seconds() / 3600) - (int(brk) / 60), 2)
            
            entry = WorkDay.query.filter_by(date=entry_date).first() or WorkDay(date=entry_date)
            entry.employer, entry.start_time, entry.end_time = emp, start, end
            entry.break_minutes, entry.total_hours = brk, hrs
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('view_data'))
        except Exception as e:
            return f"Error: {e}. Make sure times are filled correctly.", 400
            
    return render_template('index.html', today=date.today(), secret=SECRET_KEY)

@app.route(f'/{SECRET_KEY}/view')
def view_data():
    # Get month and year from URL parameters, default to current month/year
    selected_month = request.args.get('month', date.today().month, type=int)
    selected_year = request.args.get('year', date.today().year, type=int)

    # Filter query by selected month and year
    all_days = WorkDay.query.filter(
        extract('month', WorkDay.date) == selected_month,
        extract('year', WorkDay.date) == selected_year
    ).order_by(WorkDay.date.desc()).all()
    
    grand_total = sum(d.total_hours for d in all_days if d.total_hours)

    # Calculate weeks (Existing logic remains same)
    weeks = []
    if all_days:
        sorted_days = sorted(all_days, key=lambda x: x.date, reverse=True)
        current_week = []
        for day in sorted_days:
            if not current_week:
                current_week.append(day)
            else:
                last_day = current_week[-1]
                if day.date.isocalendar()[1] != last_day.date.isocalendar()[1] or \
                   day.date.year != last_day.date.year:
                    weeks.append({'days': current_week, 'total': sum(d.total_hours for d in current_week)})
                    current_week = [day]
                else:
                    current_week.append(day)
        weeks.append({'days': current_week, 'total': sum(d.total_hours for d in current_week)})

    # Generate a list of available months for the picker (last 12 months)
    # This helps the user see which months they can actually select
    available_months = []
    for i in range(1, 13):
        available_months.append({
            'num': i,
            'name': datetime(2000, i, 1).strftime('%B')
        })

    return render_template('view.html', 
                           weeks=weeks, 
                           grand_total=grand_total, 
                           secret=SECRET_KEY,
                           current_month=selected_month,
                           current_year=selected_year,
                           available_months=available_months)

@app.route(f'/{SECRET_KEY}/admin')
def admin():
    all_days = WorkDay.query.order_by(WorkDay.date.desc()).all()
    return render_template('admin.html', days=all_days, secret=SECRET_KEY)

@app.route(f'/{SECRET_KEY}/delete/<int:id>')
def delete_entry(id):
    db.session.delete(WorkDay.query.get_or_404(id))
    db.session.commit()
    return redirect(url_for('admin'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
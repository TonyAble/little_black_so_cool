from flask import Flask
from flask import render_template
from openpyxl import load_workbook

app = Flask(__name__)


@app.route('/index.html')
def index():
    wb = load_workbook('static/tmp.xlsx')
    sheet = wb.active
    content = []
    for row in sheet.rows:
        cell_list = []
        for cell in row:
            cell_list.append(cell.value)
        content.append(cell_list)
    wb.close()
    return render_template('index.html', content=content)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

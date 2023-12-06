from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
def manage():
    single_results = [
        {
            'rank': '1',
            'reward': '0đ'
        },
        {
            'rank': '2',
            'reward': '3.000đ'
        },
        {
            'rank': '3',
            'reward': '5.000đ'
        },
        {
            'rank': '4',
            'reward': '6.000đ'
        },
        {
            'rank': '5',
            'reward': '8.000đ'
        },
        {
            'rank': '6',
            'reward': '8.000đ'
        },
        {
            'rank': '7',
            'reward': '10.000đ'
        },
        {
            'rank': '8',
            'reward': '10.000đ'
        },
        {
            'rank': 'Tổng',
            'reward': '50.000đ'
        }
        
    ]

    couple_results = [
        {
            'rank': '1',
            'reward': ''
        },
        {
            'rank': '2',
            'reward': ''
        },
        {
            'rank': '3',
            'reward': ''
        },
        {
            'rank': '4',
            'reward': ''
        },
        {
            'rank': 'Tổng',
            'reward': ''
        }
    ]

    errors = [
        {
            'name': 'Ngừng thi đấu lý do không thuyết phục số đông',
            'error': 'Xếp hạng cuối giải, phạt 15.000đ'
        }
    ]


    return render_template('main.html', single_results=single_results, couple_results=couple_results, errors=errors)
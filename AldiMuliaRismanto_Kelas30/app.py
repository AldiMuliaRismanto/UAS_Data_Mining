import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

model_file = open('Fifa.pkl', 'rb')
model = pickle.load(model_file)


@app.route('/')
def index():
    return render_template('fifa.html', output='belum diprediksi')


@app.route('/predict', methods=['POST'])
def predict():
    Team1,Team2, Team1_FIFA_RANK , Team2_FIFA_RANK ,   Team1_Goalkeeper_Score ,  Team2_Goalkeeper_Score ,  Team1_Defense ,  Team2_Defense ,  Team1_Offense , Team2_Offense , Team1_Midfield , Team2_Midfield , Team1_Result   = [
        x for x in request.form.values()]
    data = []

    data.append(str(Team1))
    data.append(str(Team2))
    data.append(int(Team1_FIFA_RANK))
    data.append(int(Team2_FIFA_RANK))
    data.append(int(Team1_Goalkeeper_Score))
    data.append(int(Team2_Goalkeeper_Score))
    data.append(int(Team1_Defense))
    data.append(int(Team2_Defense))
    data.append(int(Team1_Offense))
    data.append(int(Team2_Offense))
    data.append(int(Team1_Midfield))
    data.append(int(Team2_Midfield))
    

    prediction = model.predict([data])
    output = (prediction[0])
    if output == 1.0:
        hasil = "Home Team Win"
    if output == 2.0:
        hasil = "Result is Draw"
    else:
        hasil = "Away Team Win"

    return render_template('fifa.html', output=hasil, Team1_FIFA_RANK=Team1_FIFA_RANK, Team2_FIFA_RANK=Team2_FIFA_RANK, Team1_Goalkeeper_Score=Team1_Goalkeeper_Score, Team2_Goalkeeper_Score=Team2_Goalkeeper_Score, Team1_Defense=Team2_Defense, Team1_Offense=Team1_Offense, Team2_Offense=Team2_Offense, Team1_Midfield=Team1_Midfield, Team2_Midfield=Team2_Midfield, Team1_Result=Team1_Result)

    if __name__ == '__main__':
        app.run(debug=True)

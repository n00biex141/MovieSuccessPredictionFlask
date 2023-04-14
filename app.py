from flask import Flask, render_template, request
import numpy as np
import pickle as pkl

app = app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def login():
    return render_template('login.html')
    
 
@app.route('/index')
def index():
    return render_template('index.html')
    

@app.route('/predict',  methods=['GET', 'POST'])
def predict():
    director = str(request.args.get('director'))
    language = str(request.args.get('language'))
    
    year = int(request.args.get('year'))    
    
    genre_action = request.args.get('action')
    genre_thriller = request.args.get('thriller')
    genre_scifi = request.args.get('scifi')
    genre_biography = request.args.get('biography')
    genre_drama = request.args.get('drama')
    genre_history = request.args.get('history')
    genre_romance = request.args.get('romance')
    genre_comdey = request.args.get('comedy')
    genre_crime = request.args.get('crime')
    genre_adventure = request.args.get('adventure')
    genre_horror = request.args.get('horror')
    genre_sport = request.args.get('sport')
    genre_fantacy = request.args.get('fantacy')
    genre_war = request.args.get('war')
    
    mrating = float(request.args.get('mrating'))
    mvotes = int(request.args.get('mvotes'))
    wwgross = float(request.args.get('wwgross'))

    with open('./model/model.pkl', 'rb') as f:
        model = pkl.load(f)
        
    with open('./model/directors.pkl', 'rb') as f:
        inv_directors = pkl.load(f)
        
    with open('./model/languages.pkl', 'rb') as f:
        inv_languages = pkl.load(f)
    
    director = inv_directors[director]
    language = inv_languages[language]
            
    genre_action = 1 if genre_action == "on" else 0
    genre_thriller = 1 if genre_thriller == "on" else 0
    genre_scifi = 1 if genre_scifi == "on" else 0
    genre_biography = 1 if genre_biography == "on" else 0
    genre_drama = 1 if genre_drama == "on" else 0
    genre_history = 1 if genre_history == "on" else 0
    genre_romance = 1 if genre_romance == "on" else 0
    genre_comdey = 1 if genre_comdey == "on" else 0
    genre_crime = 1 if genre_crime == "on" else 0
    genre_adventure = 1 if genre_adventure == "on" else 0
    genre_horror = 1 if genre_horror == "on" else 0
    genre_sport = 1 if genre_sport == "on" else 0
    genre_fantacy = 1 if genre_fantacy == "on" else 0
    genre_war = 1 if genre_war == "on" else 0    
        
    arr = np.array([
        director,
        language,
        year,
        genre_action,
        genre_thriller,
        genre_scifi,
        genre_biography,
        genre_drama,
        genre_history,
        genre_romance,
        genre_comdey,
        genre_crime,
        genre_adventure,
        genre_horror,
        genre_sport,
        genre_fantacy,
        genre_war,
        mrating,
        mvotes,
        wwgross
    ]).reshape(1, -1)
    
    print(arr)
    
    predict = model.predict(arr)

    return render_template('index.html', data=predict)

if __name__ == "__main__":
    app.run(debug=True)
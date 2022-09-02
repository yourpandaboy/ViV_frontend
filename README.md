![image](https://github.com/yourpandaboy/ViV_frontend/blob/master/images/rsz_1intro_shot.jpg)

I think we all know how traditional dating websites match you with checkbox preferences based on interests. Wouldn’t it more fun if your matches vibe with you? Using your bio, with the help of our friendly NLP model, this web app understands your personality and finds matches that will vibe with you.

Introducing ViV! An unsupervised learning project trained from 60,000 OkCupid profiles from [Kaggle](https://www.kaggle.com/datasets/andrewmvd/okcupid-profiles).

After weeks of research 🧐, trials & errors, and insane amount of coffee ☕️ , Java-based MALLET gave the best result to classify 60,000 profiles into 19 topics!

![image](https://github.com/yourpandaboy/ViV_frontend/blob/master/images/rsz_viv_wordcloud2_8_24.jpg)

By converting the model to Python-based LDA, ViV gets your required information (bio is the most important) and does its magic to allocate your bio within the 19 groups. Finally returns you profiles you are highly correlated within those groups (WordCloud topics).

App home: https://projectviv28.herokuapp.com/

![image](https://github.com/yourpandaboy/ViV_frontend/blob/master/images/matches3.jpg)

# Tech Stack
### Front End
- <a href="https://streamlit.io/">Streamlit</a>
- <a href="https://www.heroku.com/">Heroku</a>

### Back End
- <a href="https://fastapi.tiangolo.com/">FastAPI</a>
- <a href="https://www.docker.com/">Docker</a>
- <a href="https://cloud.google.com/">Google Cloud Platform</a>


### Machine Learning Tools
- <a href="https://mallet.cs.umass.edu/index.php/Main_Page">JAVA MALLET</a>
- <a href="https://www.nltk.org/index.html">nltk </a>
- <a href="https://radimrehurek.com/gensim/">Gensim </a>
- <a href="https://spacy.io/">Spacy </a>


# Special thanks
- <a href="https://github.com/mechworrior">Tony</a>

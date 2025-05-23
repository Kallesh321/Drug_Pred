#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pickle import load
import flask as f
from pandas import DataFrame


# In[2]:


app = f.Flask(__name__)
model = load(open("model.pkl","rb"))


# In[ ]:


@app.route("/")
def home():
    return f.render_template("index3.html")


# In[ ]:


@app.route("/predict",methods=["POST"])
def predict():
    A=[]
    for i in f.request.form.values():
        A.append(float(i))
    predicted_profit = model.predict(DataFrame([[A[0],A[1]]]))[0]
    return f.render_template("index3.html",pred = predicted_profit )


# In[ ]:


if __name__=="__main__":
    app.run(debug=True)
    


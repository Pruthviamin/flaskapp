#!/usr/bin/env python
# coding: utf-8

# # Flask

# In[2]:


from flask import Flask


# In[3]:


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World! This is my first website :)"

if __name__ == "__main__":
    app.run()


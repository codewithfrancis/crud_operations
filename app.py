from components import app 

# importing each app blue print 
from components.home.ui import index
from components.blog.ui import blog

app.register_blueprint(blog, url_prefix="/")
app.register_blueprint(index)

if __name__ == '__main__':
    app.run(debug=True)
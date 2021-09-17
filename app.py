from components import app 

# importing each app blue print 
from components.home.ui import index
from components.blog.ui import blog

app.register_blueprint(index)
app.register_blueprint(blog)

if __name__ == '__main__':
    app.run(debug=True)
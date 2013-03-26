from Bisection import bisection
from Parser import parse_string

import wsgiref.handlers

from google.appengine.api import users
from google.appengine.ext import webapp

class MainHandler(webapp.RequestHandler):
    formstring = '''<form method="post" action="/">
                <p>Enter Function : <input type="text" name="fun"/></p>
                <p>Enter X1 (0):    <input type="text" name="x1"/></p>
                <p>Enter X2 (1): <input type="text" name="x2"/></p>
                <p><input type="submit" value= "Hesapla"></p>
                <h4>Demos:</h4>
                <ul>
                  <li>x^3 - 10x^2 + 5</li>
                  <li>x1 = 0, x2 = 1</li>
                </ul>
                <ul>
                  <li>x^3 + 4x^2 - 1</li>
                  <li>x1 = 0, x2 = 1</li>
                </ul>
                <ul>
                  <li>x^3 + 4x^2 - 10</li>
                  <li>x1 = 1, x2 = 2</li>
                </ul>
                <ul>
                  <li>x^3 - x - 3</li>
                  <li>x1 = 1, x2 = 2</li>
                </ul>
                
                </form>'''

    def fx(self, x, coef_list):
            return float(\
coef_list[len(coef_list)- 1]*x**(len(coef_list)-1) + \
coef_list[len(coef_list)- 2]*x**(len(coef_list)-2) + \
coef_list[len(coef_list)- 3]*x**(len(coef_list)-3) + \
coef_list[len(coef_list)- 4]*x**(len(coef_list)-4))
    
    
    def get(self):
        user = users.get_current_user()
        title = "Bisection method"
        if user:
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write("""<html>
                                <head>
                                    <title>""" + title + """</title> 
                                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                            </head>
                            <body BGCOLOR=\#CC9966>""")
            
            self.response.out.write('<h2>Bisection method</h2>')
            
            self.response.out.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
        self.response.out.write(self.formstring)
        self.response.out.write('</body></html>')

    def post(self):
        fun = self.request.get('fun')
        coef_list = parse_string(fun)
        
        x1 = self.request.get('x1')
        x2 = self.request.get('x2')
        
        x1 = float(x1)
        x2 = float(x2)
        root = bisection(self.fx, coef_list, x1, x2,)
        gercek_kok = float(root)    
        self.response.out.write('<p>Root ~= '+ str(gercek_kok) +'</p>\n')
        
def main():
    application = webapp.WSGIApplication([
                                          ('/.*', MainHandler)],
                                         debug=True)
    wsgiref.handlers.CGIHandler().run(application)
            
if __name__ == '__main__':
    main()
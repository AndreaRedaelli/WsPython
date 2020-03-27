import cherrypy
import pandas as pd
import MyProcessor
class WebService(object):
    p = None

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    #example of curl on window to enquire the ws 
    # curl -d "{"""num1""" : [1, 2, 3], """num2""":[4, 5, 6]}" -H "Content-Type: application/json" -X POST http://localhost:8080/process
    def process(self):
      data = cherrypy.request.json
      df = pd.DataFrame(data)
      output = self.p.run(df)
      return output.to_json()
    
    @cherrypy.expose
    def webPage(self):
        return "<b> Hello World </b>"

    def __init__(self):
        self.p = MyProcessor.MyProcessor()

if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(WebService())
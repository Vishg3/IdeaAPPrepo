from flask import Flask,request

app=Flask(__name__)

ideas={
   1: {
       'id':1,
       'idea_name':'ONDC',
       'idea_description':'Details about ONDC',
       'idea_author':'Vishnu'
    },
    2: {
       'id':2,
       'idea_name':'Save Soil',
       'idea_description':'Details about Saving Soil',
       'idea_author':'Mark'
    }
}

@app.get('/ideaapp/api/v1/ideas')
def get_all_ideas():
    idea_author=request.args.get('idea_author')
    if idea_author:
        idea_res={}
        for key,value in ideas.items():
            if value['idea_author']==idea_author:
                idea_res[key]=value
        return idea_res
    return ideas

@app.post('/ideaapp/api/v1/ideas')
def create_idea():
    try:
        request_body=request.get_json()
        if request_body['id'] and request_body['id'] in ideas:
            return 'idea with the same id already present',400
        ideas[request_body['id']]=request_body
        return 'idea created and saved successfully',201
    except KeyError:
        return 'id is missing',400
    except:
        return 'Some internal server error',500

@app.get('/ideaapp/api/v1/ideas/<idea_id>')    
def get_idea_id(idea_id):
    try:
        if int(idea_id) in ideas:
            return ideas[int(idea_id)],200
        else:
            return 'Idea id passed is not present',400
    except:
        return 'Some internal error happened',500

@app.put('/ideaapp/api/v1/ideas/<idea_id>')
def update_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas[int(idea_id)]=request.get_json()
            return ideas[int(idea_id)],200
        else:
            return 'Idea id passed is not present',400
    except:
        return 'Some internal error happened',500

@app.delete('/ideaapp/api/v1/ideas/<idea_id>')
def delete_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas.pop(int(idea_id))
            return 'Idea got successfully removed'
        else:
            return 'Idea id passed is not present',400
    except:
        return 'Some internal error happened',500



if __name__=='__main__':
    app.run(port=8080)
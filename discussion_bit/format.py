import json
import hashlib

class DiscussionBit:
    """this is, imo, the discussion bit, the smallest possible indivisible unit of a discussion
    
    It's purpose is to provide a format to store any kind of discussion in a more structured way than raw text and to offer a reliable interface for automated interpretation.
    
    I have thought about this for some time and there are some things I want to share to justify that this, and only this, is the appropriate definition:
    
    * something is being said
    True
    
    * this can be independent of context and author, but there should be an option to specify both
    True is True indepently of who said it or where
    
    * for discussion purposes it's necessary to link to context
    B says (A says "True") is False
    
    * for processing and reasoning, it's necessary to combine different statements and for that you always need two plus an operator.
    
    The user would be free to use 'text' as an operator and 'context' and 'other' as objects for the operation.
    
    e.g. text=merge context=master other=thepatch
    
    * for processing 'text' and 'context', if it is not 'None', should be converted to a hexhash and the object should be saved as hexhash.txt with the content being str(DiscussionBit), which is a json dump of the strings or string conversions of the parts.
    
    * all data inside this object should be strings, because all relevant data or identifiers can be converted to strings.
    
    e.g. 
    context can be a url, a scientific DOI or a natural expression that refers to some place and time or something
    author can be a email, a name, the name of an organization if it's a press release, the name of a newspaper
    
    * it being convertable to strings leverages existing tech, e.g. encryption, and enables it to be shared across virtually all known channels, e.g. email.
    
    * most the contents are up to probably interpretation anyway and even if they're not, it's better to leave hard coded interpretations to users of the format. That is, this format should NOT limit what users do with it by hardcoding some interpretations here.
    
    e.g. you can set up some automated reasoning with this, and I intend to, like
    
    (B says "not (A says "True") ") evaluating to 'False'
    
    and then I would be able to use 'not' and 'True' in an automated way.
    
    * BUT there is virtually no limit to what one might want to automatically interpret this way and how, so it's better to leave that to the individual interpretation.
    
    reusing an example from above, you might want 
    
    e.g. text='merge' context='master' other='thepatch'
    text='merge context into other' context='master' other='thepatch'
    text='merge other into context' context='master' other='thepatch'
    text='merge other into master' context='master' other='thepatch'
    text='merge into master' context='thepatch'
    
    all of which can make sense in the right context.
    """
    def __init__(self,text,context=None,other=None,author=None,hexhash=None):
        self.text=text
        self.context=context
        self.other=other
        self.author=author
        self.hexhash=hexhash
    
    def __eq__(self,other):
        if type(other)!=type(self):
            return False
        if self.text==other.text:
            return True
        return False
        
    def update_hexhash(self):
        if self.context!=None:
            hexhash=hashlib.sha256((self.text+self.context).encode())
        else:
            hexhash=hashlib.sha256(self.text.encode())
        self.hexhash=hexhash.hexdigest()
            
    def __repr__(self):
        
        d={'text':self.text,
            'context':self.context,
            'other':self.other,
            'author':self.author,
            'hexhash':self.hexhash}
            
        return json.dumps(d)
        
def from_json(json_str):
    d=json.loads(json_str)
    return DiscussionBit(**d)
    a=1
        
def test():
    Dbit=DiscussionBit("Yellow")
    print(Dbit)
    Dbit.update_hexhash()
    eh=str(Dbit)
    print(eh)
    new=from_json(eh)
    print(new)
    print(Dbit==new)
    
if __name__=="__main__":
    test()

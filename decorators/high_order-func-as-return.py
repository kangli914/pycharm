
"""return the fucntion as the result of other functions"""
""" https://www.youtube.com/watch?v=kr0mpwqttM0"""

def html_tag(tag):

    # here tag will be "rememberred" by the wrapper even after html_tag funciton finished
    # This is the concept of a closure
    def wrapper(msg):
            # tag here is call free variables as it was not defined in the scope of wrapper

        print(f"<{tag}>{msg}></{tag}>")
    return wrapper

# at this point, we simply just created a new function and we haven't called or executed it of p_tag at this monment
p_tag = html_tag("p")

# at this point, p_tag == wrapper function (as it was what it returned)
# we treat p_tag function(is a function) just like wrapper function here
# so wrapper fucntion takes `msg` as argument then p_tag message so takes `msg` as arguments
print(p_tag)
print(p_tag.__name__)
# <function html_tag.<locals>.wrapper at 0x7f767a222680>
# wrapper

# here "this is p tag message" in p_tag() is pass to --> "msg" in wrapper() innner function
p_tag("this is p tag message")
# print(p_tag)
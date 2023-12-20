### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

      -Python is often used for server-side applications, data analysis, artificial intelligence, and scientific computing. JavaScript is primarily used for client-side scripting in web browsers, though it can also be used on the server-side with Node.js.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

      1. Using the get method: value = dictionary.get('c', default_value). This returns default_value if 'c' is not in the dictionary.

      2. Using try-except block:

- What is a unit test?

      A unit test is a type of software testing where individual units or components of a software are tested. The purpose is to validate that each unit of the software performs as designed. A unit is the smallest testable part of any software and usually has one or a few inputs and usually a single output.

- What is an integration test?

      An integration test is a level of software testing where individual units are combined and tested as a group. The purpose is to expose faults in the interaction between integrated units. Test drivers and test stubs are used to assist in integration testing.

- What is the role of web application framework, like Flask?

      A web application framework like Flask provides tools, libraries, and technologies to help developers build web applications. It handles much of the web development process, such as URL routing, request and response handling, and session management, allowing developers to focus on application logic rather than low-level details.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

- How do you collect data from a URL placeholder parameter using Flask?

    Route Parameters: Use them for essential or identifying information that defines the nature of the request, such as the ID of a resource (/foods/pretzel).

    Query Parameters: Use them for optional, non-identifying information that influences the operation but isn't essential for defining the resource itself (foods?type=pretzel).

- How do you collect data from the query string using Flask?

    You can define the route with a placeholder and then access the value in your view function. For example:
      @app.route('/foods/<food_id>')
      def get_food(food_id):
          # Use 'food_id' here

- How do you collect data from the body of the request using Flask?

      Use Flask's request.args to access query string parameters:
      
      @app.route('/foods')
      def get_foods():
          food_type = request.args.get('type')
           # Use 'food_type' here


- What is a cookie and what kinds of things are they commonly used for?

A cookie is a small piece of data sent from a website and stored on the user's computer by the user's web browser while the user is browsing. Cookies are used for session management, personalization, and tracking user behavior.

- What is the session object in Flask?

The session object in Flask is a way to store information specific to a user from one request to the next. Unlike cookies, session data is stored on the server. Sessions are implemented on top of cookies in Flask and provide a way to remember information from one request to another.

- What does Flask's `jsonify()` do?

Flask's jsonify() function is used to send JSON responses from a Flask view function. It turns the JSON output into a Flask response object with the application/json mimetype, which is essential for returning JSON in a HTTP response.

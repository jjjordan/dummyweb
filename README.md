
# dummyweb

Dummyweb is a dummy webserver that logs all incoming requests, header
values, and POST data.  It responds with 200 OK and a body of `OK`.  It
listens on port <b>5000</b>.

It is intended for debugging web server setups in Docker, usually by putting
it in the place of another container to see what requests that container
would see coming in.

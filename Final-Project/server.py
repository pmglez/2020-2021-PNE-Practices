import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils as SU
import requests
import json

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested:", path_name)
        print("Parameters:", arguments)

        # In this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        try:
            if path_name == "/":
                contents = SU.read_template_html_file("./html/index.html").render()
                content_type = "text/html"

            elif path_name == "/listSpecies":
                if "limit" in arguments.keys() and len(arguments) == 1:
                    limit_species = arguments["limit"][0]
                    if limit_species.isdigit() and int(limit_species) > 0:
                        contents = SU.list_species(limit_species, json_param=False)
                    else:
                        contents = SU.read_template_html_file("./html/Error.html").render()
                    content_type = "text/html"
                elif "limit" and "json" in arguments.keys() and arguments["json"][0] == "1" and len(arguments) == 2:
                    limit_species = arguments["limit"][0]
                    contents = SU.list_species(limit_species, json_param=True)
                    contents = json.dumps(contents)
                    content_type = "application/json"
                else:
                    contents = SU.read_template_html_file("./html/Error.html").render()
                    content_type = "text/html"
                print(contents)

            elif path_name == "/karyotype":
                if "specie" in arguments.keys() and len(arguments) == 1:
                    specie = arguments["specie"][0]
                    contents = SU.information_karyotype(specie, json_param=False)
                    content_type = "text/html"
                elif "specie" and "json" in arguments.keys() and arguments["json"][0] == "1" and len(arguments) == 2:
                    specie = arguments["specie"][0]
                    contents = SU.information_karyotype(specie, json_param=True)
                    contents = json.dumps(contents)
                    content_type = "application/json"
                else:
                    contents = SU.read_template_html_file("./html/Error.html").render()
                    content_type = "text/html"
                print(contents)

            elif path_name == "/chromosomeLength":
                if "specie" and "chromo" in arguments.keys() and len(arguments) == 2:
                    specie = arguments["specie"][0]
                    chromosome = arguments["chromo"][0]
                    contents = SU.chromosome_length(specie, chromosome, json_param=False)
                    content_type = "text/html"
                elif "specie" and "chromo" and "json" in arguments.keys() and arguments["json"][0] == "1" \
                        and len(arguments) == 3:
                    specie = arguments["specie"][0]
                    chromosome = arguments["chromo"][0]
                    contents = SU.chromosome_length(specie, chromosome, json_param=True)
                    contents = json.dumps(contents)
                    content_type = "application/json"
                else:
                    contents = SU.read_template_html_file("./html/Error.html").render()
                    content_type = "text/html"
                print(contents)

            elif path_name == "/geneSeq":
                if "gene" in arguments.keys() and len(arguments) == 1:
                    gene = arguments["gene"][0]
                    contents = SU.gene_seq(gene, json_param=False)
                    content_type = "text/html"
                elif "gene" and "json" in arguments.keys() and arguments["json"][0] == "1" and len(arguments) == 2:
                    gene = arguments["gene"][0]
                    contents = SU.gene_seq(gene, json_param=True)
                    contents = json.dumps(contents)
                    content_type = "application/json"
                else:
                    contents = SU.read_template_html_file("./html/Error.html").render()
                    content_type = "text/html"
                print(contents)

            elif path_name == "/geneInfo":
                if "gene" in arguments.keys() and len(arguments) == 1:
                    gene = arguments["gene"][0]
                    contents = SU.gene_info(gene, json_param=False)
                    content_type = "text/html"
                elif "gene" and "json" in arguments.keys() and arguments["json"][0] == "1" and len(arguments) == 2:
                    gene = arguments["gene"][0]
                    contents = SU.gene_info(gene, json_param=True)
                    contents = json.dumps(contents)
                    content_type = "application/json"
                else:
                    contents = SU.read_template_html_file("./html/Error.html").render()
                    content_type = "text/html"
                print(contents)

            elif path_name == "/geneCalc":
                if "gene" in arguments.keys() and len(arguments) == 1:
                    gene = arguments["gene"][0]
                    contents = SU.gene_calc(gene, json_param=False)
                    content_type = "text/html"
                elif "gene" and "json" in arguments.keys() and arguments["json"][0] == "1" and len(arguments) == 2:
                    gene = arguments["gene"][0]
                    contents = SU.gene_calc(gene, json_param=True)
                    contents = json.dumps(contents)
                    content_type = "application/json"
                else:
                    contents = SU.read_template_html_file("./html/Error.html").render()
                    content_type = "text/html"
                print(contents)

            else:
                contents = SU.read_template_html_file("./html/Error.html").render()
                content_type = "text/html"

        except requests.exceptions.HTTPError:
            contents = SU.read_template_html_file("./html/Error.html").render()
            print(contents)
            content_type = "text/html"
        except KeyError:
            contents = SU.read_template_html_file("./html/Error.html").render()
            print(contents)
            content_type = "text/html"

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(contents.encode())))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

# ----------------------
#  Useful variables
# ----------------------
NORM=\033[0m
BOLD=\033[1m
CHECK=\033[32m✔\033[39m
port=5000


# ----------------------
#  Default build
# ----------------------
build:
	@echo "\n⚡  ${BOLD}This might take a minute${NORM}  ⚡\n"
	@make boot
	@cd bootstrap; mv bootstrap/* ../
	@echo "\n${BOLD}Move files...  ${NORM}${CHECK}\n"
	@rm -rf bootstrap
	@make index
	@make js
	@echo "\n⚡  ${BOLD}Good luck building your site${NORM}  ⚡\n"


# ----------------------
#  Clone Bootstrap && Make
# ----------------------
boot:
	@git clone git://github.com/twitter/bootstrap.git
	@echo "\n${BOLD}Clone Twitter Bootstrap...  ${NORM}${CHECK}\n"
	@cd bootstrap; make bootstrap
	@cd bootstrap; cp -R less bootstrap/css/less


# ----------------------
#  rm -rf all the things!
# ----------------------
clean:
	@rm -rf {bootstrap,css,img,js}


# ----------------------
#  Compile CSS
# ----------------------
css:
	@cd css; cat bootstrap.min.css > production.css
	@cd css; cat bootstrap-responsive.min.css >> production.css
	@cd css; recess --compress dev.less >> production.css
	@echo "\n⚡  ${BOLD}Don't forget to update index.html${NORM}  ⚡\n"


# ----------------------
#  Set up the index.html file
# ----------------------
index:
	@curl -L http://git.io/index > index.html
	@echo "\n${BOLD}Create index.html...  ${NORM}${CHECK}\n"
	@touch css/dev.less
	@echo "${BOLD}Create blank dev.less file...  ${NORM}${CHECK}\n"


# ----------------------
#  Installer check
# ----------------------
install:
	@echo "\n${BOLD}You're all good!${NORM}\n"


# ----------------------
#  External JavaScript
# ----------------------
js:
	@curl http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js > js/jquery.js
	@echo "\n${BOLD}Grab latest jQuery...  ${NORM}${CHECK}\n"
	@curl -L http://git.io/less-1.3.0 > js/less.js
	@echo "\n${BOLD}Grab latest LESS.js...  ${NORM}${CHECK}\n"


# ----------------------
#  Github Pages build
# ----------------------
pages:
	@echo "\n⚡  ${BOLD}Installing for Github Pages${NORM}  ⚡\n"
	@touch README.md
	@git init && git add --all && git commit -am "First commit" && git checkout -b gh-pages
	@make build


# ----------------------
#  Simple Python server
# ----------------------
serve:
	@python -m SimpleHTTPServer ${port}


# ----------------------
#  Compile Less files on save
# ----------------------
watch:
	@echo "\n${BOLD}Watching dev.less...  ${NORM}\n"
	@echo "watch('css/.*\.less') { system 'make css' }" > /tmp/bootstrap.watchr
	@watchr /tmp/bootstrap.watchr


.PHONY: css js

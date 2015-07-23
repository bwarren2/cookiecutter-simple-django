"use strict";
module.exports = {
     options: {
      // Task-specific options go here.
    },
    all: {
        src: [
            "dist/release.css",
        ].map(function(filename){return "{{cookiecutter.repo_name}}/static/"+filename;}),
        dest: "{{cookiecutter.repo_name}}/static/dist/styles.css"
    },
}

"use strict";
module.exports = {
    options: {
      separator: ";\n",
    },
    dist: {
        src: [
            "bower_components/jquery/dist/jquery.min.js",
            "bower_components/bootstrap/dist/js/bootstrap.min.js",
            // "js/charting.js",
            "js/project.js",
        ].map(function(file){ return "{{cookiecutter.repo_name}}/static/"+file;}),
      dest: "{{cookiecutter.repo_name}}/static/dist/built.js",
    },
};

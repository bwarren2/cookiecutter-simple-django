"use strict";
module.exports = {
    styles: {
      files: [
        "{{cookiecutter.repo_name}}/static/css/*.less",
        "{{cookiecutter.repo_name}}/static/css/project/*.less"
      ], // which files to watch
      tasks: ["less", "cssmin", "concat_css"],
      options: {
        nospawn: true
      }
    },
    js: {
      files: [
        "js/*.js",
        "bower_components/**/*.js",
      ].map(function(filename){return "{{cookiecutter.repo_name}}/static/"+filename;}),
      tasks: ["concat"],
      options: {
        nospawn: true
      }
    }
}

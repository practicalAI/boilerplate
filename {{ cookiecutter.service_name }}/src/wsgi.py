from {{ cookiecutter.package_name }}.application import application

if __name__ == "__main__":
    application.run(host=application.config['HOST'],
                    port=application.config['PORT'],
                    debug=application.config['DEBUG'])

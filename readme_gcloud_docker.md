 STEPS TO DO BEFORE THIS
 1. change PORT in app.py 
 script: app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
 2. Init and create or choose account, project 
 bash script: gcloud init
 3. add Dockerfile with a specifications to run in gcloud in a directory
 4. run scripts in docker.sh file
 to run entire file you can make it executable first, and then run
 chmod +x docker.sh
 ./docker.sh



 for help visit this url
 https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service?authuser=2

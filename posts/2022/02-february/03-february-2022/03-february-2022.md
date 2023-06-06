
To create an Azure CI/CD pipeline for building and deploying an Angular application, you can follow these steps:

Step 1: Set up your Azure DevOps Project

1.  Sign in to the Azure DevOps portal (dev.azure.com) using your Azure account.
2.  Create a new project or select an existing project.

Step 2: Configure the Build Pipeline

1.  Navigate to the Pipelines section in your Azure DevOps project.
2.  Click on the "New Pipeline" button to create a new pipeline.
3.  Choose the repository where your Angular application code is hosted (e.g., Azure Repos, GitHub, Bitbucket).
4.  Select the branch that you want to build.
5.  Choose the template for your pipeline. You can search for "Angular" or "Node.js" templates.
6.  Select the template that best suits your needs (e.g., "Node.js with Angular").
7.  Review and update the pipeline configuration as required, such as specifying the version of Node.js and Angular to use.
8.  Save and run the pipeline to ensure it builds successfully.

Step 3: Configure Azure Pipeline Variables

1.  Define any necessary pipeline variables. For example, you might need to specify the Azure subscription and resource group where your application will be deployed.
2.  Go to the pipeline settings and navigate to the "Variables" tab.
3.  Add the required variables and their values. These variables will be used in subsequent pipeline tasks.

Step 4: Add Deployment Steps

1.  After the build step, you can add deployment tasks to deploy the Angular application to Azure.
2.  Add an Azure App Service Deployment task to deploy the built application to an Azure Web App.
3.  Configure the deployment task with the appropriate settings, such as the Azure subscription, resource group, and web app name.

Step 5: Save and Run the Pipeline

1.  Save your pipeline configuration.
2.  Trigger a manual or automated build to test the pipeline.
3.  Monitor the pipeline execution and ensure that the build and deployment steps complete successfully.

Step 6: Test and Verify the Deployed Application

1.  Once the pipeline has successfully completed, navigate to your Azure Web App to verify that the Angular application is deployed correctly.
2.  Test the deployed application to ensure it functions as expected.

By following these steps, you can create an Azure CI/CD pipeline for building and deploying your Angular application. Remember to adapt the pipeline to your specific requirements, such as configuring additional build steps, running tests, or incorporating other deployment targets.
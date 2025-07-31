# Deploying to Render

This application is configured for easy deployment to [Render](https://render.com/) using Docker. Follow these steps to deploy the application.

## 1. Create a New Web Service

1.  From the Render dashboard, click the **New +** button and select **Web Service**.
2.  Connect your Git repository where this project is hosted. You can either connect a new repository or select an existing one.

## 2. Configure the Service

On the configuration page, fill in the following details:

-   **Name**: Choose a name for your service (e.g., `metadata-eraser`).
-   **Region**: Select a region close to you or your users.
-   **Branch**: Select the branch you want to deploy (e.g., `main`).
-   **Runtime**: Select **Docker**. Render will automatically detect the `Dockerfile` in your repository.
-   **Instance Type**: Choose an instance plan. The `Free` plan is suitable for personal projects and testing.

Render will automatically handle the `PORT` environment variable, so you do not need to set it manually.

## 3. Deploy

1.  Click the **Create Web Service** button at the bottom of the page.
2.  Render will start building your application from the `Dockerfile` and deploy it. You can monitor the progress in the deploy logs.
3.  Once the deployment is complete, your application will be live at the URL provided by Render (e.g., `https://your-service-name.onrender.com`).

That's it! Your application is now running on Render. Render will also automatically redeploy your application whenever you push changes to the configured branch.
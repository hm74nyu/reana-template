REANA Workflow Templates
========================

**REANA Workflow Templates** are parameterized workflow specifications for the [Reproducible research data analysis platform (REANA)](http://reanahub.io/). Workflow templates are primarily intended use cases that allow users to run pre-defined REANA workflows using their own input files and parameters.

The template contains a REANA workflow specification and a list of parameter declarations. Parameters may be referenced in the workflow specification. The idea is that we use the parameter declarations for example in a front-end to renader a form that allows the user to enter their own data which get uploaded to the server. Then generate a valid REANA workflow specification by replacing references to the parameters with submitted values which is then bein executed on a REANA cluster.

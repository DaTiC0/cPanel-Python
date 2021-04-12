# cPanel-Python

Cpanel UAPI Python client

## just in case

use python to comunicate with cpanel


`https://hostname.example.com:2083/cpsess##########/execute/Module/function?parameter=value&parameter=value&parameter=value`

/execute/Module/function?parameter=value&parameter=value&parameter=value
> [!NOTE]
> 
*MODULE and FINCTIONS are static just for now*

### Create an API token

You can use one of the following methods to create an API token:

Use cPanel’s Manage API Tokens interface (cPanel >> Home >> Security >> Manage API Tokens).

Use the UAPI Tokens::create_full_access function.
{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import zeep\
\
# Set the WSDL URL\
wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"\
\
# Set method URL\
method_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryIntPhoneCode"\
\
# Set service URL\
service_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"\
\
# Create the header element\
header = zeep.xsd.Element(\
	"Header",\
	zeep.xsd.ComplexType(\
		[\
			zeep.xsd.Element(\
				"\{http://www.w3.org/2005/08/addressing\}Action", zeep.xsd.String()\
			),\
			zeep.xsd.Element(\
				"\{http://www.w3.org/2005/08/addressing\}To", zeep.xsd.String()\
			),\
		]\
	),\
)\
# Set the header value from header element\
header_value = header(Action=method_url, To=service_url)\
\
# Initialize zeep client\
client = zeep.Client(wsdl=wsdl_url)\
\
# Set country code for Denmark\
# Just change to the country you want UK/US/SE\
country_code = "SE"\
\
# Make the service call\
result = client.service.CountryIntPhoneCode(\
	sCountryISOCode=country_code,\
	_soapheaders=[header_value]\
)\
# Print the result\
print(f"Phone Code for \{country_code\} is \{result\}")}
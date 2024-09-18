import requests
import json


def obtenerIpDesdeDominio(dominio):
    """
    Obtiene la dirección IP de un dominio y la región en la que se encuentra esa IP.

    Args:
        dominio (str): El dominio del cual se desea obtener la IP y la región.

    Returns:
        None
    """
    # Imprime el dominio que se está buscando
    print("------------Dominio ->" + str(dominio) + "------------")

    # Realiza una solicitud GET a la API de NetworkCalc para obtener registros DNS del dominio

    resultadoBusqueda = requests.get("https://networkcalc.com/api/dns/lookup/" + str(dominio))

    # Verifica que la respuesta contiene registros DNS

    if resultadoBusqueda.json()['records'] is not None:

        # Recorre los registros de tipo 'A' (dirección IPv4)
        for i in range(len(resultadoBusqueda.json()['records']['A'])):

            # Obtiene la dirección IP del primer registro 'A'
            ip = resultadoBusqueda.json()['records']['A'][0]['address']

            # Realiza una solicitud GET a la API de IPinfo para obtener información sobre la IP
            resultadoRegion = requests.get("https://ipinfo.io/" + str(ip) + "/json")

            # Imprime la región asociada con la IP
            print("La región de la IP -> " + str(ip) + " es " + str(resultadoRegion.json()['region']))


# Lista de dominios de empresas para los que se desea obtener información de IP
dominios_empresas = [
    "dianeandgeordi.com"
]


# Llama a la función 'obtenerIpDesdeDominio' para cada dominio en la lista
# Descomentar la siguiente línea para ejecutar la función para cada dominio
# for i in dominios_empresas:
#     obtenerIpDesdeDominio(i)

def obtenerEmailsDesdeDominio(dominio):
    """
    Obtiene y muestra los correos electrónicos asociados a un dominio utilizando la API de Hunter.io.

    Args:
        dominio (str): El dominio del cual se desean obtener los correos electrónicos.

    Returns:
        None
    """
    # Reemplazar 'stripe.com' con el dominio deseado y 'api_key' con la clave de API válida

    resultadoEmails = requests.get(
        "https://api.hunter.io/v2/domain-search?domain=" + dominio + "&api_key=2cbb2d89c8208ff0f606a96aae1739d333c585fc")

    # Imprime los correos electrónicos en formato JSON
    print(json.dumps(resultadoEmails.json()['data']['emails'], indent=4))

    # Verifica que la respuesta contiene correos electrónicos
    if resultadoEmails.json()['data']['emails'] is not None:
        # Recorre la lista de correos electrónicos y los imprime
        for correo in range(len(resultadoEmails.json()['data']['emails'])):
            print("Correo: " + str(resultadoEmails.json()['data']['emails'][correo]['value']))


# Llama a la función 'obtenerEmailsDesdeDominio' con un dominio de ejemplo
obtenerEmailsDesdeDominio("dianeandgeordi.com")

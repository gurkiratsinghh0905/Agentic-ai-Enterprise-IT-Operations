def software_lookup(name):

    approved = {

        "zoom":"approved",

        "teams":"approved",

        "chrome":"approved"
    }

    return approved.get(
        name.lower(),
        "not approved"
    )
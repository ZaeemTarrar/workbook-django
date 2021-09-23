def object_has_attr(obj, attr):
    try:
        if obj[str(attr)]:
            return True
        else:
            return False
    except:
        return False


A = {
    "b": {
        "c": "zaeem"
    }
}

print(object_has_attr(A, "b"))

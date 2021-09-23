def object_has_attr(obj, attr):
    try:
        if obj[str(attr)]:
            return True
        else:
            return False
    except:
        return False


def validate_body_parts(body, parts):
    try:
        if parts is None:
            parts = []
        if isinstance(parts, list):
            flag = True
            msgs = []
            for part in parts:
                if not object_has_attr(body, part):
                    msg = str('`{}`'.format(part))
                    print("Msg: ", part, msg, hasattr(body, part))
                    flag = False
                    msgs.append(msg)
            word = "is" if len(msgs) == 1 else "are"
            msgs = ((", ".join(msgs)) + "  {} required").format(word)
            final_msg = "Warning: {}".format(msgs)
            return flag, final_msg
        else:
            return False, None
    except:
        return False, None

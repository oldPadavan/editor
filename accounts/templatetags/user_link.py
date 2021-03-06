from django import template

register = template.Library()

@register.inclusion_tag('links/user.html')
def user_link(user, text=None, new_window=False):
    if text is None:
        text = user.get_full_name() if user.is_active else 'Deactivated user'
    return {'user': user, 'text': text, 'new_window': new_window}

@register.inclusion_tag('links/user_thumbnail.html')
def user_thumbnail(user, size=None, glyphicon_size=None, link=False):
    if not user.is_active:
        return {
            'link': False,
            'has_avatar': False,
            'user': user,
            'size': size
        }
    avatar = user.userprofile.avatar
    if size is None:
        size = 20
    if glyphicon_size is None:
        glyphicon_size = size
    context = {'user': user, 'size': size, 'glyphicon_size': glyphicon_size, 'link': link}
    if not avatar:
        context['has_avatar'] = False
    else:
        context['has_avatar'] = True
        context['image_url'] = user.userprofile.avatar.url if size is None else user.userprofile.avatar.thumbnail(size)
    return context

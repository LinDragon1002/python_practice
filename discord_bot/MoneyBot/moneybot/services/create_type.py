from web_app.models import items_types
def create_type_async(name: str):
    # 先檢查是否已存在
    exists = items_types.objects.filter(items=name).aexists()
    if exists:
        content = f"❗ 類型 **{name}** 已存在"
    else:
        instance = items_types.objects.acreate(items=name)
        content = f"✅ 類型 **{name}** 已建立 (ID {instance.id})"
    return content
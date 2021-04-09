import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from message.models import MessageBoard


# Create your views here.
def index(request):
    content = MessageBoard.objects.filter(mb_isShow=True)
    context = {
        "name": '姜开鑫',
        "content": content
    }
    return render(request, template_name="index.html", context=context)


def add(request):
    if request.method.upper() == "POST":  # 检测是否是POST请求
        result = {}  # 存放返回的数据
        data = {}
        msg = request.POST.get("message")
        if msg:
            # 添加留言内容
            m = MessageBoard()
            m.mb_content = msg
            m.save()
            data['id'] = m.id
            data['message'] = msg
            result['code'] = 200
            result['text'] = "留言添加成功"

        else:
            result['code'] = 400
            result['text'] = "添加失败，请检查是否提交了数据"

        result['data'] = data
        return HttpResponse(json.dumps(result), content_type="application/json")

    return redirect(reverse("index"))


def delete(request):
    if request.method.upper() == "POST":
        result = {}
        msg_id = request.POST.get("msg_id")
        if msg_id:
            msg = MessageBoard.objects.filter(id=msg_id)
            if msg:
                msg.delete()
                result['code'] = 200
                result['text'] = "删除成功"
            else:
                result['code'] = 400
                result['text'] = "删除失败，可能是该留言已经被删除了~"

            return HttpResponse(json.dumps(result), content_type="json/application")
        result['code'] = 400
        result['text'] = "请提供正确的留言ID~"
        return HttpResponse(json.dumps(result), content_type="json/application")

    return redirect(reverse("index"))

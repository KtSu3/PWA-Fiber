from ninja import NinjaAPI, Schema
from API.models import FirstQuery, SecondQuery, LogSearch
from typing import List
from typing import Optional
import uuid

api_post = NinjaAPI(version='1.0-post')

class PostSchema(Schema):
    name: str
    slot: int
    pon: int
    onu: int
    onu_distance: str
    query_id: Optional[str]
    status: str
    signal: str
    user: str


class PostSearchSchema(Schema):
     search: str
     user: str

    
@api_post.post('/writesearch')
def write_search(request, posts: List[PostSearchSchema]):
    data = []
    print(data)
    for post in  posts:
        post_instance = LogSearch(
            search = post.search,
            user=post.user

        )
        post_instance.save()
        print(post_instance)
        data.append({"search": post.search, "user": post.user})
        print(data)
    return { 'data': data}


@api_post.post('/writefirstquery')
def write_first_query(request, posts: List[PostSchema]):
    data = []

    query_id = uuid.uuid4()  

    for post in posts:
        post_instance = FirstQuery(
            query_id=query_id,
            name=post.name,
            slot=post.slot,
            pon=post.pon,
            onu=post.onu,
            onu_distance=post.onu_distance,
            status=post.status,
            signal=post.signal,
            user=post.user
        )
        post_instance.save()

        data.append({
            "query_id": str(query_id),
            "name": post.name,
            "slot": post.slot,
            "pon": post.pon,
            "onu": post.onu,
            "onu_distance": post.onu_distance,
            "status": post.status,
            "signal": post.signal,
            "user": post.user
        })

    return {"data": data, "query_id": str(query_id)}

@api_post.post('/writesecondquery')
def write_second_query(request, posts: List[PostSchema]):
    data = []
    query_id = uuid.uuid4()

    for post in posts:
        post_instance = SecondQuery(
            query_id=query_id,
            name=post.name,
            slot=post.slot,
            pon=post.pon,
            onu=post.onu,
            onu_distance=post.onu_distance,
            status=post.status,
            signal=post.signal,
            user=post.user
        )
        post_instance.save()

        data.append({
            "query_id": str(query_id),
            "name": post.name,
            "slot": post.slot,
            "pon": post.pon,
            "onu": post.onu,
            "onu_distance": post.onu_distance,
            "status": post.status,
            "signal": post.signal,
            "user": post.user
        })

    return {"data": data}
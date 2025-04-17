from views.writer_views import WriterAPI



def reguster_routes(app):
    
    writer_view = WriterAPI.as_view("Writer_api")
    app.add_url_rule("/api/Writers", defaults={"writer_id": None}, view_func=writer_view, methods=["GET"])
    app.add_url_rule("/api/Writers/<int:writer_id>", view_func=writer_view, methods=["GET"])
    
    
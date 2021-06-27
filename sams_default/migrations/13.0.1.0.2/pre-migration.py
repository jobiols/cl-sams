def migrate(cr, version):
    """ inexplicable error en modulo document
    """
    cr.execute("""
        insert into documents_tag
            (id,folder_id,facet_id,name)
        VALUES
            (9,15,12,'tag agregado para que no reviente')
    """)
    
    cr.execute("""
        insert into documents_tag
            (id,folder_id,facet_id,name)
        VALUES
            (3,15,12,'otro tag agregado para que no reviente');
    """)

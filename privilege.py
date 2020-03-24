import falcon
import simplejson as json
import mysql.connector
import config


class PrivilegeCollection:
    @staticmethod
    def __init__():
        pass

    @staticmethod
    def on_options(req, resp):
        resp.status = falcon.HTTP_200

    @staticmethod
    def on_get(req, resp):
        cnx = mysql.connector.connect(**config.myems_user_db)
        cursor = cnx.cursor()

        query = (" SELECT id, name, data "
                 " FROM tbl_privileges "
                 " ORDER BY id DESC ")
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        cnx.disconnect()

        result = list()
        if rows is not None and len(rows) > 0:
            for row in rows:
                meta_result = {"id": row[0],
                               "name": row[1],
                               "data": row[2]}
                result.append(meta_result)

        resp.body = json.dumps(result)

    @staticmethod
    def on_post(req, resp):
        """Handles POST requests"""
        try:
            raw_json = req.stream.read().decode('utf-8')
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.EXCEPTION', description=ex)

        new_values = json.loads(raw_json, encoding='utf-8')

        cnx = mysql.connector.connect(**config.myems_user_db)
        cursor = cnx.cursor()
        add_row = (" INSERT INTO tbl_privileges "
                   "             (name, data) "
                   " VALUES (%s, %s) ")

        cursor.execute(add_row, (new_values['data']['name'],
                                 new_values['data']['data'],
                                 ))
        new_id = cursor.lastrowid
        cnx.commit()
        cursor.close()
        cnx.disconnect()

        resp.status = falcon.HTTP_201
        resp.location = '/privileges/' + str(new_id)


class PrivilegeItem:
    @staticmethod
    def __init__():
        pass

    @staticmethod
    def on_options(req, resp, id_):
        resp.status = falcon.HTTP_200

    @staticmethod
    def on_delete(req, resp, id_):
        if not id_.isdigit() or int(id_) <= 0:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description='API.INVALID_PRIVILEGE_ID')

        cnx = mysql.connector.connect(**config.myems_user_db)
        cursor = cnx.cursor()

        # check relationship with users
        cursor.execute(" SELECT id "
                       " FROM tbl_users "
                       " WHERE privilege_id = %s ", (id_,))
        rows_users = cursor.fetchall()
        if rows_users is not None and len(rows_users) > 0:
            cursor.close()
            cnx.disconnect()
            raise falcon.HTTPError(falcon.HTTP_400,
                                   title='API.BAD_REQUEST',
                                   description='API.THERE_IS_RELATIONSHIP_WITH_USERS')

        cursor.execute(" SELECT name "
                       " FROM tbl_privileges "
                       " WHERE id = %s ", (id_,))
        if cursor.fetchone() is None:
            cursor.close()
            cnx.disconnect()
            raise falcon.HTTPError(falcon.HTTP_404, title='API.NOT_FOUND',
                                   description='API.PRIVILEGE_NOT_FOUND')

        # TODO: delete associated objects
        cursor.execute(" DELETE FROM tbl_privileges WHERE id = %s ", (id_,))
        cnx.commit()

        cursor.close()
        cnx.disconnect()

        resp.status = falcon.HTTP_204

    @staticmethod
    def on_put(req, resp, id_):
        """Handles PUT requests"""
        try:
            raw_json = req.stream.read().decode('utf-8')
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.EXCEPTION', description=ex)

        if not id_.isdigit() or int(id_) <= 0:
            raise falcon.HTTPError(falcon.HTTP_400, title='API.BAD_REQUEST',
                                   description='API.INVALID_PRIVILEGE_ID_')

        new_values = json.loads(raw_json, encoding='utf-8')

        cnx = mysql.connector.connect(**config.myems_user_db)
        cursor = cnx.cursor()

        cursor.execute(" SELECT name "
                       " FROM tbl_privileges "
                       " WHERE id = %s ", (id_,))
        if cursor.fetchone() is None:
            cursor.close()
            cnx.disconnect()
            raise falcon.HTTPError(falcon.HTTP_404, title='API.NOT_FOUND',
                                   description='API.PRIVILEGE_NOT_FOUND')

        update_row = (" UPDATE tbl_privileges "
                      " SET name = %s, data = %s "
                      " WHERE id = %s ")
        cursor.execute(update_row, (new_values['data']['name'],
                                    new_values['data']['data'],
                                    id_,))
        cnx.commit()

        cursor.close()
        cnx.disconnect()

        resp.status = falcon.HTTP_200

from config.conexao_bd import db

class ListarDeclaracoes:
    pipeline = [
        {
            '$group': {
                '_id': '$MES_OBITO', 
                'count': {
                    '$sum': 1
                }
            }
        }, 
        {
            '$sort': {
                '_id': 1
            }
        }
    ]
    
    async def aggregate(self, ano: str, match: object = None):
        if match:
            self.pipeline['$match'] = match
        res = await db[ano].aggregate(self.pipeline).to_list(12)
        return res
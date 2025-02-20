from code.Background import Background
from code.const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level-um-bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'level-um-bg{i + 1}', (0, 0)))
                    list_bg.append(Background(f'level-um-bg{i + 1}', (WIN_WIDTH, 0)))
                return list_bg

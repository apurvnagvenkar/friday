from data_architecture.general_information.age import age_entities
from data_architecture.general_information.occupation import occupation_entities


def get_entities_for_intent(intent, entities):
    """

    :param intent:
    :return:
    """
    entities_for_intent = {}
    dict = {
    'age': age_entities.entities,
    'occupation': occupation_entities.entities

    }
    print '******* %s %s '%(intent, entities)
    for entity in entities['entity_data']:
        if entity in dict.get(intent, []):
            if entity:
                entities_for_intent[entity] = entities['entity_data'][entity][0]['entity_value']
            else:
                entities_for_intent[entity] = None
    return entities_for_intent

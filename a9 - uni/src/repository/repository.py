from src.repository.repository_exception import RepositoryException


class Repository:
    def __init__(self):
        self._data = {}

    def add(self, element):
        if element.id in self._data:
            raise RepositoryException(f"Element with id {element.id} already exists!")
        self._data[element.id] = element

    def remove(self, element_id):
        if element_id not in self._data:
            raise RepositoryException(f"Element with id {element_id} does not exist!")
        del self._data[element_id]

    def update(self, element):
        if element.id not in self._data:
            raise RepositoryException(f"Element with id {element.id} does not exist!")
        self._data[element.id] = element

    def get_all(self):
        return list(self._data.values())
    def search_after_id(self, id):
        list_of_instances = []

        id = str(id)

        for obj in self._data.values():
            obj_id = str(obj.id)
            if id in obj_id:
                list_of_instances.append(obj)

        return list_of_instances

    def search_after_name(self, name):
        list_of_instances = []

        name = name.lower()

        for obj in self._data.values():
            obj_name = obj.name.lower()
            if name in obj_name:
                list_of_instances.append(obj)

        return list_of_instances

    def search_after_title(self, title):
        list_of_instances = []

        title = title.lower()

        for obj in self._data.values():
            obj_title = obj.title.lower()
            if title in obj_title:
                list_of_instances.append(obj)

        return list_of_instances

    def search_after_author(self, author):
        list_of_instances = []

        author = author.lower()

        for obj in self._data.values():
            obj_author = obj.author.lower()
            if author in obj_author:
                list_of_instances.append(obj)

        return list_of_instances

    def search(self, field_to_search_for):
        """
        Searches the data for the given field_to_search_for.

        :param field_to_search_for: The field to search for.

        :return: A list of elements that partially (or fully) match the given field_to_search_for (case insensitive).
        """
        field_to_search_for = field_to_search_for.lower()
        matching_elements = []

        for element in self._data.values():
            for attribute in element.__dict__.values():
                if field_to_search_for in str(attribute).lower():
                    matching_elements.append(element)

        return matching_elements

    def delete_all(self):
        self._data.clear()
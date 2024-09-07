"""
This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values,
which represents that the prerequisites of courseId are courseIds.
Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []},
should return ['CSC100', 'CSC200', 'CSCS300'].
"""


def sort_courses(course_dict):
    visit_dict = {}
    course_order = []

    def helper(course, prereqs, curr_order=[]):
        if course in visit_dict and visit_dict[course] is 'visited':
            # course visited so prereq completed
            return curr_order

        if course in visit_dict and visit_dict[course] is 'visiting':
            # ERROR must be a loop, return none
            return None

        visit_dict[course] = 'visiting'  # set course we are look at to visiting

        if len(prereqs) == 0:
            # if no prereqs required for this course then set to 'visited' and return the course
            visit_dict[course] = 'visited'
            return curr_order + [course]

        # loop over all the prereq courses to find their prereqs
        for c in prereqs:
            curr_order = helper(c, course_dict[c], curr_order)
            if curr_order is None:
                # if curr_order is None, that means a loop was found, return None
                return None

        visit_dict[course] = 'visited'
        return curr_order + [course]

    for course, prereqs in course_dict.items():
        course_order = helper(course, prereqs, course_order)
        if course_order is None:
            return None

    return course_order


if __name__ == '__main__':
    # ['CSC100', 'CSC200', 'CSC300']
    print(sort_courses({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}))

    # ['CSC100', 'CSC200', 'CSC300', 'CSC700', 'CSC400', 'CSC800', 'CSC500']
    print(sort_courses({
        'CSC500': ['CSC300', 'CSC400', 'CSC800'],
        'CSC800': ['CSC700'],
        'CSC400': ['CSC700'],
        'CSC300': ['CSC100', 'CSC200'],
        'CSC700': [],
        'CSC200': [],
        'CSC100': []}))

    # ['CSC100', 'CSC200', 'CSC400', 'CSC300']
    print(sort_courses({
        'CSC400': ['CSC200'],
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': []
    }))

    # None
    print(sort_courses({
        'CSC400': ['CSC300'],
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': ['CSC400']
    }))
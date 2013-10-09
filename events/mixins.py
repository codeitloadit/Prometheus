class WorkflowCompareMixin(object):
    '''
    Provides a implementation of comparing objects in a workflow. The ordinal required to make this
    work is not defined here. Users should be sure to define an attribute `ordinal`.
    '''
    # Originally designed with order and work order workflow in mind.
    # The ordinal required to make this work is not defined here because it would force it to be
    # a database field and reference objects would not work.
    #
    # Python docs reminded me that users of this mixin may also need to override __hash__. I don't
    # think this is necessary since these comparisons are for convenience and not absolute.
    #
    def __eq__(self, other):
        '''
        Returns True when `self` is ordered the same as `other`. Returns NotImplemented when
        `other` cannot be compared to `self`.
        '''
        return self.ordinal == other.ordinal

    def __ge__(self, other):
        '''
        Returns True when `self` is ordered after or the same as `other`. Returns NotImplemented
        when `other` cannot be compared to `self`.
        '''
        return self.ordinal >= other.ordinal

    def __gt__(self, other):
        '''
        Returns True when `self` is ordered after `other`. Returns NotImplemented when `other`
        cannot be compared to `self`.
        '''
        return self.ordinal > other.ordinal

    def __le__(self, other):
        '''
        Returns True when `self` is ordered before or the same as `other`. Returns NotImplemented
        when `other` cannot be compared to `self`.
        '''
        return self.ordinal <= other.ordinal

    def __lt__(self, other):
        '''
        Returns True when `self` is ordered before `other`. Returns NotImplemented when `other`
        cannot be compared to `self`.
        '''
        return self.ordinal < other.ordinal

class ReferenceEvent(WorkflowCompareMixin):
    '''
    Stub object that can be used to compare an event against a known state.
    '''
    # Inheriting from WorkflowCompareMixin allows comparisons to be a two-way street.
    #
    # Use reference objects so that we don't have to store this reference data in the db, requiring
    # extra db trips. You might subclass ReferenceEvent and use it to instantiate Events with common
    # data.
    #
    # Using a special reference event might be appropriate when you want events included in your
    # app that exist outside the workflow. More on this later.
    #
    def __init__(self, name, ordinal):
        self.name = name
        self.ordinal = ordinal

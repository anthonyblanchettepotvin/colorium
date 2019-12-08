"""Module used to check if a string respects a set of rules described in a naming convention."""

from abc import ABCMeta, abstractmethod, abstractproperty
import re as regex


class NamingConventionError(Exception):
    """Base class for exceptions in this module."""

    pass


class IntruderError(NamingConventionError):
    """
    Raised when a name variable doesn't match any rule.

    Attributes:
        variable -- The variable that didn't match any rule.
        message -- Explanation of the error.
    """

    def __init__(self, variable, message):
        super(IntruderError, self).__init__(variable, message)

        self.variable = variable
        self.message = message


class DuplicateRuleError(NamingConventionError):
    """
    Raised when the same rule is added twice to the list of rules.

    Attributes:
        rule -- The rule that was added a second time.
        message -- Explanation of the error.
    """

    def __init__(self, rule, message):
        super(DuplicateRuleError, self).__init__(rule, message)

        self.rule = rule
        self.message = message


class DuplicateNameError(NamingConventionError):
    """
    Raised when two rules with the same name are added to the list of rules.

    Attributes:
        name -- The name of the rules.
        message -- Explanation of the error.
    """

    def __init__(self, name, message):
        super(DuplicateNameError, self).__init__(name, message)

        self.name = name
        self.message = message


class TooManyVariablesError(NamingConventionError):
    """
    Raised when the name to evaluate has more variables than the number of rules.

    Attributes:
        variable_count -- The number of variables in the name.
        rule_count -- The number of rules in the list.
        message -- Explanation of the error.
    """

    def __init__(self, variable_count, rule_count, message):
        super(TooManyVariablesError, self).__init__(variable_count, rule_count, message)

        self.variable_count = variable_count
        self.rule_count = rule_count
        self.message = message


class NotEnoughVariablesError(NamingConventionError):
    """
    Raised when the name to evaluate has lesss variables than the number of mandatory rules.

    Attributes:
        variable_count -- The number of variables in the name.
        rule_count -- The number of mandatory rules in the list.
        message -- Explanation of the error.
    """

    def __init__(self, variable_count, rule_count, message):
        super(NotEnoughVariablesError, self).__init__(variable_count, rule_count, message)

        self.variable_count = variable_count
        self.rule_count = rule_count
        self.message = message


class BadValueError(NamingConventionError):
    """
    Raised when the user tries to set a rule's value to something that doesn't match the rule.

    Attributes:
        rule_name -- The name of the rule.
        value -- The value passed by the user.
        message -- Explanation of the error.
    """

    def __init__(self, rule_name, value, message):
        super(BadValueError, self).__init__(rule_name, value, message)

        self.rule_name = rule_name
        self.value = value
        self.message = message


class NamingConvention(object):
    """Object that uses a set of rules to check if the naming convention is respected by the name."""

    @property
    def rules(self):
        """The list of rules."""

        return self.__rules


    @property
    def separator(self):
        """The separator used to separate each variable in the name."""

        return self.__separator


    @property
    def mandatory_rules(self):
        """The list of mandatory rules."""

        return [rule for rule in self.rules if not rule.optional]


    @property
    def optional_rules(self):
        """The list of optional rules."""

        return [rule for rule in self.rules if rule.optional]


    @property
    def rules_met(self):
        """The list of rules that are met."""

        return [rule for rule in self.rules if rule.met]


    @property
    def rules_not_met(self):
        """The list of rules that are not met."""

        return [rule for rule in self.rules if not rule.met]


    @property
    def reconstructed_name(self):
        """The name back to it's original state."""

        reconstructed_name = ''

        for rule in self.rules_met:
            reconstructed_name += rule.formatted_value
            reconstructed_name += self.separator if rule is not self.rules_met[-1] else ''

        return reconstructed_name


    def __init__(self, rules=None, separator='_'):
        self.__rules = rules if rules else []
        self.__separator = separator


    def add_rule(self, rule):
        """
        Adds a rule to the list.

        Parameters :
            rule -- The rule to add to the list of rules.
        """

        if self.rule_exists(rule.name):
            raise DuplicateNameError(rule.name, 'Cannot have two rules with the same name.')

        if rule not in self.rules:
            self.rules.append(rule)
        else:
            raise DuplicateRuleError(rule, 'Cannot add the same rule twice.')


    def rule_exists(self, name):
        """
        Checks if a rule already exists.

        Parameters :
            name -- The name of the rule.

        Result :
            Returns True if one rule with the same name exists, False otherwise.
        """

        for rule in self.rules:
            if rule.name == name:
                return True

        return False


    def remove_rule(self, rule):
        """
        Deletes a rule from the list.

        Parameters :
            rule -- The rule to remove from the list of rules.
        """

        if rule in self.rules:
            self.rules.remove(rule)


    def get_rule(self, name):
        """
        Returns a rule by its name.

        Parameters :
            name -- The rule's name to return.

        Result :
            Returns the rule if it finds it, returns None otherwise.
        """

        result = None

        for rule in self.rules:
            if rule.name == name:
                result = rule
                break

        return result


    def evaluate_name(self, name):
        """
        Checks if all the rules of the naming convention are met by the name.

        Parameters :
            name -- The name to evaluate.

        Result :
            Returns True if all the mandatory rules are met, False if not.
        """

        variables = name.split(self.separator)

        if len(variables) > len(self.rules):
            raise TooManyVariablesError(len(variables), len(self.rules), 'The name has too many variables.')

        if len(variables) < len(self.mandatory_rules):
            raise NotEnoughVariablesError(len(variables), len(self.mandatory_rules), 'The name doesn\'t have enough variables.')

        for variable in variables:
            if not self.apply_rules(variable):
                raise IntruderError(variable, 'The variable \'{}\' doesn\'t match any of the naming convention rules.'.format(variable))

        return self.all_mandatory_rules_met()


    def apply_rules(self, variable):
        """
        Applies all the rules that are not met to the variable.

        Parameters :
            variable -- The variable to apply the rules to.

        Result :
            Returns True if one of the rules is met, False otherwise.
        """

        for rule in self.rules_not_met:
            if rule.evaluate_variable(variable):
                return True

        return False


    def all_mandatory_rules_met(self):
        """
        Checks if all the mandatory rules are met.

        Result :
            Returns True if all the mandatory rules are met, False if not.
        """

        for rule in self.mandatory_rules:
            if not rule.met:
                return False

        return True


    def all_rules_met(self):
        """
        Checks if all the rules are met.

        Result :
            Returns True if all the rules are met, False if not.
        """

        for rule in self.rules:
            if not rule.met:
                return False

        return True


    def reset(self):
        """Resets all the rules to their default state."""

        for rule in self.rules:
            rule.reset()


class Rule(object):
    """Object that determine if a part of the name matches a specified format."""

    __metaclass__ = ABCMeta


    @abstractproperty
    def name(self):
        """The name of the rule."""

        pass


    @abstractproperty
    def met(self):
        """The result of the rule."""

        pass


    @abstractproperty
    def value(self):
        """The value of the rule."""

        pass


    @abstractproperty
    def optional(self):
        """Indicates if the rule is optional or mandatory."""

        pass


    @abstractproperty
    def formatted_value(self):
        """The value back in it's initial form."""

        pass


    @abstractmethod
    def evaluate_variable(self, variable):
        """
        Checks if the rule is respected by the variable.

        Parameters:
            variable -- The variable to evaluate.
        """

        pass


    @abstractmethod
    def reset(self):
        """Resets the rule to its default state."""

        pass


class RegexRule(Rule):
    """Object that determine if a part of the name matches a regular expression."""

    @property
    def name(self):
        return self.__name


    @property
    def met(self):
        return self.__met


    @property
    def value(self):
        return self.__value


    @property
    def optional(self):
        return self.__optional


    @property
    def formatted_value(self):
        return self.__value


    @property
    def expression(self):
        """The regular expression used to validate the rule."""

        return self.__expression


    def __init__(self, name, expression, optional=False):
        self.__name = name
        self.__met = False
        self.__value = ''
        self.__expression = expression
        self.__optional = optional


    def evaluate_variable(self, variable):
        result = regex.search(self.expression, variable)

        if result:
            print 'Rule \"{}\" met with variable \"{}\"'.format(self.__name, variable)

            self.__value = result.group()
            self.__met = True

        return self.met


    def reset(self):
        self.__met = False
        self.__value = ''


class MultipleRegexRule(Rule):
    """Object that determine if a part of the name matches one of multiple regular expressions."""

    @property
    def name(self):
        return self.__name


    @property
    def met(self):
        return self.__met


    @property
    def value(self):
        return self.__value


    @property
    def optional(self):
        return self.__optional


    @property
    def formatted_value(self):
        return self.__value


    @property
    def expressions(self):
        """The list of regular expressions used to validate the rule."""

        return self.__expressions


    def __init__(self, name, expressions=None, optional=False):
        self.__name = name
        self.__met = False
        self.__value = ''
        self.__expressions = expressions if expressions else []
        self.__optional = optional


    def evaluate_variable(self, variable):
        for expression in self.expressions:
            result = regex.search(expression, variable)

            if result:
                print 'Rule \"{}\" met with variable \"{}\"'.format(self.__name, variable)

                self.__value = result.group()
                self.__met = True

                break

        return self.met


    def reset(self):
        self.__met = False
        self.__value = ''


class InternalNamingConventionRule(Rule):
    """Object that determine if a part of the name respects a nested naming convention."""

    @property
    def name(self):
        return self.__name


    @property
    def met(self):
        return self.__met


    @property
    def value(self):
        return self.__value


    @property
    def optional(self):
        return self.__optional


    @property
    def formatted_value(self):
        return self.naming_convention.reconstructed_name


    @property
    def naming_convention(self):
        """The naming convention used internally by the rule."""

        return self.__naming_convention


    def __init__(self, name, optional=False, rules=None, separator='-'):
        self.__name = name
        self.__met = False
        self.__value = {}
        self.__optional = optional

        self.__naming_convention = NamingConvention(rules, separator)


    def add_rule(self, rule):
        """
        Adds a rule to the list.

        Parameters :
            rule -- The rule to add to the list of rules.
        """

        self.naming_convention.add_rule(rule)


    def remove_rule(self, rule):
        """
        Deletes a rule from the list.

        Parameters :
            rule -- The rule to remove from the list of rules.
        """

        self.naming_convention.remove_rule(rule)


    def get_rule(self, name):
        """
        Returns a rule by its name.

        Parameters :
            name -- The rule's name to return.

        Result :
            Returns the rule if it finds it, returns None otherwise.
        """

        self.naming_convention.get_rule(name)


    def evaluate_variable(self, variable):
        try:
            self.__met = self.naming_convention.evaluate_name(variable)
        except IntruderError:
            return self.met

        if self.met:
            for rule in self.naming_convention.rules:
                if rule.met:
                    self.__value[rule.name] = rule.value

        return self.met


    def reset(self):
        for rule in self.naming_convention.rules:
            rule.reset()


NC = NamingConvention()

RULE_TYPE = RegexRule('type', r'^[a-z]{3}$', False)
NC.add_rule(RULE_TYPE)

RULE_NAME = RegexRule('name', r'^[a-zA-Z]+$', True)
NC.add_rule(RULE_NAME)

RULE_VARIANT = MultipleRegexRule('variant', [r'^\d{2}$', r'^[a-zA-Z]+$'], True)
NC.add_rule(RULE_VARIANT)

RULE_SCENE_SHOT = InternalNamingConventionRule('scene_shot', True)
NC.add_rule(RULE_SCENE_SHOT)

RULE_SCENE = RegexRule('scene', r'^\d{3}$', False)
RULE_SCENE_SHOT.add_rule(RULE_SCENE)

RULE_SHOT = RegexRule('shot', r'^\d{3}$', True)
RULE_SCENE_SHOT.add_rule(RULE_SHOT)

RULE_VERSION = MultipleRegexRule('version', [r'^v\d{3}$', r'^publish$', r'^export$'], False)
NC.add_rule(RULE_VERSION)

print NC.evaluate_name('mdl_policeCar_crashed_010_v001')

print NC.reconstructed_name

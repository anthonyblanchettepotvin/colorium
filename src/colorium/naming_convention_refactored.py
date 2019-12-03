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


class NamingConvention(object):
    """Object that uses a set of rules to check if the naming convention is respected by the name."""

    @property
    def rules(self):
        """The list of rules."""

        return self.__rules


    @property
    def mandatory_rules(self):
        """The list of mandatory rules."""

        mandatory_rules = []

        for rule in self.__rules:
            if not rule.optional:
                mandatory_rules.append(rule)

        return mandatory_rules


    def __init__(self, rules=None):
        self.__rules = rules if rules else []


    def add_rule(self, rule):
        """Adds a rule to the list."""

        if self.rule_exists(rule.name):
            raise DuplicateNameError(rule.name, 'Cannot have two rules with the same name.')

        if rule not in self.__rules:
            self.__rules.append(rule)
        else:
            raise DuplicateRuleError(rule, 'Cannot add the same rule twice.')


    def rule_exists(self, name):
        """Checks if a rule already exists.

        Parameters :
            name -- The name of the rule.

        Result :
            Returns True if one rule with the same name exists, False otherwise.
        """

        for rule in self.__rules:
            if rule.name == name:
                return True

        return False


    def remove_rule(self, rule):
        """Deletes a rule from the list."""

        if rule in self.__rules:
            self.__rules.remove(rule)


    def evaluate_name(self, name):
        """Checks if all the rules of the naming convention are met by the name.

        Parameters :
            name -- The name to evaluate.

        Result :
            Returns True if all the mandatory rules are met, False if not.
        """

        variables = name.split('_')

        if len(variables) > len(self.__rules):
            raise TooManyVariablesError(len(variables), len(self.__rules), 'The name has too many variables.')

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

        for rule in self.__rules:
            if not rule.met:
                if rule.evaluate_variable(variable):
                    return True

        return False


    def all_mandatory_rules_met(self):
        """
        Checks if all the mandatory rules are met.

        Result :
            Returns True if all the mandatory rules are met, False if not.
        """

        for rule in self.__rules:
            if not rule.met and not rule.optional:
                return False

        return True


    def all_rules_met(self):
        """
        Checks if all the rules are met.

        Result :
            Returns True if all the rules are met, False if not.
        """

        for rule in self.__rules:
            if not rule.met:
                return False

        return True


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


    @abstractmethod
    def evaluate_variable(self, variable):
        """Checks if the rule is respected by the variable."""

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

        return self.__met


class ComposedRegexRule(Rule):
    """Object that determine if a part of the name composed by multiple sub-variables each matches a regular expression."""

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


    def __init__(self, name, optional=False, rules=None, separator=''):
        self.__name = name
        self.__met = False
        self.__value = {}
        self.__optional = optional
        self.__rules = rules if rules else []
        self.__separator = separator


    def add_rule(self, rule):
        """Adds a rule to the list."""

        if rule not in self.__rules:
            self.__rules.append(rule)


    def remove_rule(self, rule):
        """Deletes a rule from the list."""

        if rule in self.__rules:
            self.__rules.remove(rule)


    def evaluate_variable(self, variable):
        sub_variables = variable.split(self.__separator)

        for sub_variable in sub_variables:
            for rule in self.__rules:
                if not rule.met:
                    if rule.evaluate_variable(sub_variable):
                        self.__value[rule.name] = rule.value
                        break

        for rule in self.__rules:
            if not rule.met and not rule.optional:
                self.__met = False
                return self.__met

        self.__met = True
        return self.__met


NC = NamingConvention()

RULE_TYPE = RegexRule('type', r'\b([a-z]{3})\b', False)
NC.add_rule(RULE_TYPE)

RULE_NAME = RegexRule('name', r'\b([a-zA-Z]+)\b', False)
NC.add_rule(RULE_NAME)

RULE_VARIANT = RegexRule('variant', r'\b([0-9]{2})\b', True)
NC.add_rule(RULE_VARIANT)

RULE_SCENE_SHOT = ComposedRegexRule('scene_shot', optional=True, separator='-')
NC.add_rule(RULE_SCENE_SHOT)

RULE_SCENE = RegexRule('scene', r'\b([0-9]{3})\b', False)
RULE_SCENE_SHOT.add_rule(RULE_SCENE)

RULE_SHOT = RegexRule('shot', r'\b([0-9]{3})\b', True)
RULE_SCENE_SHOT.add_rule(RULE_SHOT)

RULE_VERSION = RegexRule('version', r'\b(v[0-9]{3})\b', False)
NC.add_rule(RULE_VERSION)

print NC.evaluate_name('mdl_policeCar_v001')

print RULE_SCENE_SHOT.value

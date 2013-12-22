# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import namedtuple

from base import QueryOperation
from params import SingleParam, StaticParam

from models import PageInfo


DabLink = namedtuple('DabLink', 'title ns dab_link dab_link_ns')

class GetQueryPage(QueryOperation):
    field_prefix = 'gqp'
    input_field = SingleParam('page')
    """
    Valid pages:

    Ancientpages, BrokenRedirects, Deadendpages, Disambiguations,
    DoubleRedirects, Listredirects, Lonelypages, Longpages, Mostcategories,
    Mostimages, Mostinterwikis, Mostlinkedcategories, Mostlinkedtemplates,
    Mostlinked, Mostrevisions, Fewestrevisions, Shortpages,
    Uncategorizedcategories, Uncategorizedpages, Uncategorizedimages,
    Uncategorizedtemplates, Unusedcategories, Unusedimages, Wantedcategories,
    Wantedfiles, Wantedpages, Wantedtemplates, Unwatchedpages, Unusedtemplates,
    Withoutinterwiki, DisambiguationPages, DisambiguationPageLinks
    """
    fields = [StaticParam('generator', 'querypage'),
              StaticParam('prop', 'info'),
              StaticParam('inprop', 'subjectid|talkid|protection')]
    output_type = PageInfo

    def extract_results(self, query_resp):
        ret = []
        for k, pid_dict in query_resp['pages'].iteritems():
            page = PageInfo.from_query(pid_dict,
                                       source=self.source)
            ret.append(page)
        return ret

    def prepare_params(self, **kw):
        params = super(GetQueryPage, self).prepare_params(**kw)
        if params.get('gqpcontinue'):
            params['gqpoffset'] = params.pop('gqpcontinue')
        return params


class GetAncientPages(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Ancientpages')]


class GetDabPageLinks(GetQueryPage):
    field_prefix = 'qp'
    input_field = None
    fields = [StaticParam('list', 'querypage'),
              StaticParam('qppage', 'DisambiguationPageLinks')]
    output_type = [DabLink]

    def extract_results(self, qp_res):
        ret = []
        for page in qp_res['querypage']['results']:
            ret.append(DabLink(page['title'],
                               page['ns'],
                               page['databaseResult']['to_namespace'],
                               page['databaseResult']['to_title']))
        return ret

class GetBrokenRedirects(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'BrokenRedirects')]


class GetDeadendPages(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Deadendpages')]


class GetDisambiguations(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Disambiguations')]


class GetDoubleRedirects(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Doulberedirects')]


class GetListRedirects(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Listredirects')]


class GetLonelyPages(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Lonelypages')]


class GetLongPages(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Longpages')]


class GetMostCategories(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Mostcategories')]


class GetMostImages(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Mostimages')]


class GetMostInterwikiLinks(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Mostinterwikis')]


class GetMostLinkedCategories(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Mostlinkedcategories')]


class GetMostLinkedTemplates(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Mostlinkedtemplates')]


class GetMostLinked(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Mostlinked')]


class GetMostRevisions(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Mostrevisions')]


class GetFewestRevisions(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Fewestrevisions')]


class GetShortPages(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Shortpages')]


class GetUncategorizedCategories(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Uncategorizedcategories')]


class GetUncategorizedPages(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Uncategorizedpages')]


class GetUncategorizedImages(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Uncategorizedimages')]


class GetUncategorizedTemplates(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Uncategorizedtemplates')]


class GetUnusedCategories(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Unusedcategories')]


class GetUnusedImages(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Unusedimages')]


class GetWantedCategories(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Wantedcategories')]


class GetWantedFiles(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Wantedfiles')]


class GetWantedPages(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Wantedpages')]


class GetWantedTemplates(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Wantedtemplates')]


class GetUnusedTemplates(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Unusedtemplates')]


class GetWithoutInterwikiLinks(GetQueryPage):
    input_field = None
    fields = GetQueryPage.fields + [StaticParam('gqppage', 'Withoutinterwiki')]

# 'Unwatchedpages' requires being logged in

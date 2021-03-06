from django.conf.urls.defaults import *

urlpatterns = patterns('siteutils.shortcuts',
    url(r'^Dashboard$', 'redirect_to_reverse', {'url': 'stats_dashboard',
                                    'permanent': True}),
    url(r'^About$', 'redirect_to_reverse', {'url': 'about',
                                    'permanent': True}),
    url(r'^PrivacyPolicy$', 'redirect_to_reverse', {'url': 'privacy',
                                    'permanent': True}),
    url(r'^Home$', 'redirect_to_reverse', {'url': 'home',
                                    'permanent': True}),
    url(r'^NewPost$', 'redirect_to_reverse', {'url': 'topic_new',
                                    'permanent': True}),
    url(r'^NewPosts$', 'redirect_to_reverse', {'url': 'topic_since_login',
                                    'permanent': True}),
    url(r'^TopKeywords$', 'redirect_to_reverse', {'url': 'topic_cloud',
                                    'permanent': True}),
    url(r'^Posts$', 'redirect_to_reverse', {'url': 'home',
                                    'permanent': True}),
    url(r'^Posts/(?P<tag>.+)$', 'redirect_to', {'url': '/tags/%(tag)s/',
                                    'permanent': True}),
    url(r'^Help$', 'redirect_to_reverse', {'url': 'about',
                                    'permanent': True}),
    url(r'^Search$', 'redirect_to_reverse', {'url': 'search',
                                    'permanent': True}),
    url(r'^AdvancedSearchResults$', 'redirect_to_reverse', {'url': 'search',
                                    'permanent': True}),
    #url(r'^ShowPost/(?P<topic_id>\d+)$', 'redirect_to_reverse', {'url': 'topic_detail', kwargs={'topic_id': '%(topic_id)d'}),
    #                                'permanent': True}),
    url(r'^ShowPost/(?P<topic_id>\d+)$', 'redirect_to', {'url': '/posts/%(topic_id)s/',
                                                         'permanent': True}),
    url(r'^SignIn$', 'redirect_to_reverse', {'url': 'acct_login',
                                    'permanent': True}),
    url(r'^TermsOfUse$', 'redirect_to_reverse', {'url': 'terms',
                                    'permanent': True}),
    url(r'^Thanks$', 'redirect_to_reverse', {'url': 'about',
                                    'permanent': True}),
    url(r'^Print/(?P<topic_id>\d+)$', 'redirect_to', {'url': '/posts/%(topic_id)s/print/',
                                    'permanent': True}),
    url(r'^Print/(?P<topic_id>\d+)/replies$', 'redirect_to', {'url': '/posts/%(topic_id)s/printreplies/',
                                    'permanent': True}),
    url(r'^AdvancedSearch$', 'redirect_to_reverse', {'url': 'search',
                                    'permanent': True}),
    url(r'^FlaggedPosts$', 'redirect_to_reverse', {'url': 'topic_watchlists',
                                    'permanent': True}),
    url(r'^EditPostWhiteboard/(?P<topic_id>\d+)$', 'redirect_to', {'url': '/posts/%(topic_id)s/',
                                    'permanent': True}),
    url(r'^FeaturedPosts$', 'redirect_to_reverse', {'url': 'topic_featured',
                                    'permanent': True}),
    url(r'^RecentWhiteboards$', 'redirect_to_reverse', {'url': 'topic_since_login',
                                    'permanent': True}),
    )

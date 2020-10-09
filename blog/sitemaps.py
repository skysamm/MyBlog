from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    """
        Django native sitemap object used for Posts
    """
    changefreq = "weekly" # hourly, monthly, never
    priority = 0.8

    def items(self):
        """
            Return the items with pusblished status
        """
        return Post.objects.filter(status=1)

    def lastmod(self, obj):
        """
            Return the date of last modification
        """
        return obj.updated_on
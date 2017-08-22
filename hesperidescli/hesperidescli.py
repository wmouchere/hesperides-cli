import click

from hesperidescli.applications import applications
from hesperidescli.applications.platforms import platforms
from hesperidescli.applications.platforms.properties import properties
from hesperidescli.applications.platforms.snapshots import snapshots
from hesperidescli.cache import cache
from hesperidescli.configure import configure
from hesperidescli.events import events
from hesperidescli.feedback import feedback
from hesperidescli.files import files
from hesperidescli.indexation import indexation
from hesperidescli.modules import modules
from hesperidescli.stats import stats
from hesperidescli.templates import templates
from hesperidescli.users import users
from hesperidescli.versions import versions


@click.group()
def cli():
    pass


cli.add_command(applications.get_application)
cli.add_command(applications.get_application_from_module)
cli.add_command(applications.perform_search_application)

cli.add_command(cache.delete_application_cache)
cli.add_command(cache.delete_applications_cache)
cli.add_command(cache.delete_modules_cache)
cli.add_command(cache.delete_release_module_cache)
cli.add_command(cache.delete_release_template_package_cache)
cli.add_command(cache.delete_templates_packages_cache)
cli.add_command(cache.delete_workingcopy_module_cache)
cli.add_command(cache.delete_workingcopy_template_package_cache)
cli.add_command(cache.regenerate_application_cache)
cli.add_command(cache.regenerate_module_cache)
cli.add_command(cache.regenerate_template_package_cache)

cli.add_command(configure.delete_profile)
cli.add_command(configure.get_conf)
cli.add_command(configure.get_profile)
cli.add_command(configure.set_conf)
cli.add_command(configure.set_profile)

cli.add_command(events.get_events)

cli.add_command(feedback.post_feedback)

cli.add_command(files.get_files)

cli.add_command(indexation.perform_reindex)

cli.add_command(modules.create_module)
cli.add_command(modules.create_module_release)
cli.add_command(modules.create_module_workingcopy_template)
cli.add_command(modules.delete_module_release)
cli.add_command(modules.delete_module_workingcopy)
cli.add_command(modules.delete_module_workingcopy_template)
cli.add_command(modules.get_module)
cli.add_command(modules.get_module_release)
cli.add_command(modules.get_module_release_template)
cli.add_command(modules.get_module_release_templates)
cli.add_command(modules.get_module_workingcopy)
cli.add_command(modules.get_module_workingcopy_template)
cli.add_command(modules.get_module_workingcopy_templates)
cli.add_command(modules.get_modules)
cli.add_command(modules.perform_search_modules)
cli.add_command(modules.search_module)
cli.add_command(modules.update_module)
cli.add_command(modules.update_module_workingcopy_template)

cli.add_command(platforms.create_application_platform)
cli.add_command(platforms.delete_application_platform)
cli.add_command(platforms.get_application_platform)
cli.add_command(platforms.perform_search_application_platforms)
cli.add_command(platforms.update_application_platform)

cli.add_command(properties.get_global_properties)
cli.add_command(properties.get_global_properties_usage)
cli.add_command(properties.get_properties)
cli.add_command(properties.get_properties_instance_model)

cli.add_command(snapshots.get_application_platform_snapshots)
cli.add_command(snapshots.restore_application_platform_snapshots)
cli.add_command(snapshots.take_application_platform_snapshot)

cli.add_command(stats.get_stats)

cli.add_command(templates.create_template_package)
cli.add_command(templates.create_template_package_workingcopy)
cli.add_command(templates.delete_template_package_release)
cli.add_command(templates.delete_template_package_workingcopy)
cli.add_command(templates.get_template_package_release)
cli.add_command(templates.get_template_package_release_model)
cli.add_command(templates.get_template_package_workingcopy)
cli.add_command(templates.get_template_package_workingcopy_model)
cli.add_command(templates.get_templates_packages_release)
cli.add_command(templates.get_templates_packages_workingcopy)
cli.add_command(templates.perform_search_templates_packages)
cli.add_command(templates.update_template_package_workingcopy)

cli.add_command(users.get_user)

cli.add_command(versions.get_versions)

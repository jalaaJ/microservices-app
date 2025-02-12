{{- /*
Return a fully qualified name for a resource by combining the chart name and the release name.
This ensures uniqueness across releases.
*/ -}}
{{- define "my-app.fullname" -}}
{{- printf "%s-%s" .Chart.Name .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- /*
Return a simple name for a resource using the chart name.
*/ -}}
{{- define "my-app.name" -}}
{{- .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
